"""
Allen TTS Platform for Home Assistant

Provides Text-to-Speech services using Allen TTS server.
"""
import logging
import requests
import voluptuous as vol

from homeassistant.components.tts import PLATFORM_SCHEMA, Provider
from homeassistant.const import CONF_HOST, CONF_PORT
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

DEFAULT_HOST = "172.30.3.9"
DEFAULT_PORT = 8000
DEFAULT_MOOD = "Sarcastic"
DEFAULT_VOICE = "allen_male" 
DEFAULT_ENGINE = "google"

CONF_MOOD = "mood"
CONF_VOICE = "voice"
CONF_ENGINE = "engine"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Optional(CONF_HOST, default=DEFAULT_HOST): cv.string,
        vol.Optional(CONF_PORT, default=DEFAULT_PORT): cv.port,
        vol.Optional(CONF_MOOD, default=DEFAULT_MOOD): cv.string,
        vol.Optional(CONF_VOICE, default=DEFAULT_VOICE): cv.string,
        vol.Optional(CONF_ENGINE, default=DEFAULT_ENGINE): cv.string,
    }
)

def get_engine(hass, config, discovery_info=None):
    """Set up Allen TTS speech component."""
    return AllenTTSProvider(hass, config)

class AllenTTSProvider(Provider):
    """Allen TTS speech api provider."""

    def __init__(self, hass, conf):
        """Initialize Allen TTS provider."""
        self.hass = hass
        self._host = conf.get(CONF_HOST, DEFAULT_HOST)
        self._port = conf.get(CONF_PORT, DEFAULT_PORT)
        self._mood = conf.get(CONF_MOOD, DEFAULT_MOOD)
        self._voice = conf.get(CONF_VOICE, DEFAULT_VOICE)
        self._engine = conf.get(CONF_ENGINE, DEFAULT_ENGINE)
        self._base_url = f"http://{self._host}:{self._port}"
        
        self.name = "Allen TTS"

    @property
    def default_language(self):
        """Return the default language."""
        return "en"

    @property
    def supported_languages(self):
        """Return list of supported languages."""
        return ["en"]

    @property
    def supported_options(self):
        """Return list of supported options."""
        return [CONF_MOOD, CONF_VOICE, CONF_ENGINE]

    def get_tts_audio(self, message, language, options=None):
        """Load TTS from Allen TTS server."""
        if options is None:
            options = {}
            
        mood = options.get(CONF_MOOD, self._mood)
        voice = options.get(CONF_VOICE, self._voice)
        engine = options.get(CONF_ENGINE, self._engine)
        
        # Prepare request data
        data = {
            "text": message,
            "mood": mood,
            "voice": voice,
            "engine": engine
        }
        
        try:
            # Send request to Allen TTS server
            url = f"{self._base_url}/speak"
            response = requests.post(
                url,
                json=data,
                headers={"Content-Type": "application/json"},
                timeout=30
            )
            
            if response.status_code == 200:
                _LOGGER.debug("Allen TTS request successful")
                # For TTS platform, we typically return audio data
                # Since Allen TTS handles playback directly, we return empty audio
                return "mp3", b""
            else:
                _LOGGER.error("Allen TTS request failed: %s", response.status_code)
                return None, None
                
        except requests.exceptions.RequestException as ex:
            _LOGGER.error("Error connecting to Allen TTS: %s", ex)
            return None, None
