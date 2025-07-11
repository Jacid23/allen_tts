# Allen TTS Integration

Integrate Allen TTS (A'Lynzz'Quorvaxth the Third) with Home Assistant for advanced text-to-speech with personality.

## Features

- **Multiple Personality Moods**: Choose from 8 different moods including Sarcastic, Happy, Dramatic, and more
- **Voice Assistant Integration**: Appears in Home Assistant Voice Assistant TTS dropdown
- **Character-Based Responses**: A'Lynzz'Quorvaxth the Third adds personality to your smart home
- **Real-Time Monitoring**: Health and queue status sensors
- **Multiple TTS Engines**: Support for Google, Piper, and System TTS engines

## Configuration

```yaml
tts:
  - platform: allen_tts
    host: "172.30.3.9"  # Your Allen TTS server IP
    port: 8000           # Server port (default: 8000)
    mood: "Sarcastic"    # Default mood (optional)
```

## Available Moods

- **Sarcastic** (default): Dry wit and sarcasm
- **Happy**: Cheerful and upbeat
- **Dramatic**: Over-the-top theatrical delivery
- **Annoyed**: Irritated tone
- **Chill**: Relaxed and laid-back
- **Excited**: High energy enthusiasm
- **Tired**: Sleepy and monotone
- **Confused**: Uncertain and questioning

## Requirements

- Allen TTS Server running on your network
- Home Assistant 2023.1.0 or newer
- Network connectivity between HA and Allen TTS server

## Usage

Once configured, Allen TTS will appear in:
- Voice Assistant configuration dropdown
- TTS service calls as `tts.allen_tts`
- Available for use in automations and scripts

Perfect for adding personality and humor to your Home Assistant voice announcements!
