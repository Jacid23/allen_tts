# Changelog

All notable changes to the Allen TTS Home Assistant Integration will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-07-10

### Added
- Initial release of Allen TTS Home Assistant Integration
- TTS platform integration for Voice Assistant dropdown
- Support for multiple personality moods:
  - Sarcastic (default)
  - Happy
  - Dramatic
  - Annoyed
  - Chill
  - Excited
  - Tired
  - Confused
- Configuration options for host, port, mood, voice, and engine
- Health status sensor (`sensor.allen_tts_status`)
- Queue status sensor (`sensor.allen_tts_queue`)
- RESTful API integration with Allen TTS server
- Support for multiple TTS engines (Google, Piper, System)
- Character-based responses from A'Lynzz'Quorvaxth the Third
- Error handling and connection management
- Debug logging support

### Technical Details
- Compatible with Home Assistant 2023.1.0+
- Uses `requests` library for HTTP communication
- Implements Home Assistant TTS Provider interface
- Provides sensor platform for status monitoring
- Follows Home Assistant integration best practices

### Configuration
- Platform: `allen_tts`
- Required: `host` parameter
- Optional: `port`, `mood`, `voice`, `engine` parameters
- Default configuration targets IoT VLAN (172.30.3.9:8000)

### Known Issues
- Custom component requires manual installation
- Server must be running and accessible on network
- Integration type is "service" (not device-based)

## [Unreleased]

### Planned Features
- HACS integration for easier installation
- Config flow for GUI-based setup
- Additional mood options
- Voice cloning support
- Audio caching for improved performance
- WebSocket support for real-time communication
- Multiple server support
- Advanced queue management

### Potential Improvements
- Config flow implementation
- Device registry integration
- Additional sensor attributes
- Performance optimizations
- Enhanced error handling
- Unit tests and CI/CD
