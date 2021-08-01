from __future__ import annotations

from typing import Optional

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

    def set_threshold(
        self, creosote_threshold: Optional[int] = None, overfire_threshold: Optional[int] = None
    ) -> None:
        if creosote_threshold is not None:
            self.creosote_threshold = creosote_threshold
        if overfire_threshold is not None:
            self.overfire_threshold = overfire_threshold

    def reset_threshold(self) -> None:
        self.creosote_threshold = CREOSOTE_THRESHOLD
        self.overfire_threshold = OVERFIRE_THRESHOLD

    def get_sensor_data(self) -> int:
        return 1
