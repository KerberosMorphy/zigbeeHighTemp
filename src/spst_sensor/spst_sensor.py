from __future__ import annotations


CREOSOTE_THRESHOLD = 0
OVERFIRE_THRESHOLD = 0
OVERFIRE_ALARM_THRESHOLD = 1.2 * OVERFIRE_THRESHOLD
BASE_LED_STATE = (True, False, False, False, False, False, False)


class SPSTSensor:
    def __init__(self) -> None:
        self.creosote_threshold = CREOSOTE_THRESHOLD
        self.overfire_threshold = OVERFIRE_THRESHOLD
        self.alarm_threshold = OVERFIRE_ALARM_THRESHOLD
        self.led_states = BASE_LED_STATE