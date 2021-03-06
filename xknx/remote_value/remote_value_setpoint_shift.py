from xknx.remote_value import RemoteValue1Count


class RemoteValueSetpointShift(RemoteValue1Count):
    """Abstraction for remote value of KNX DPT 6.010"""

    def __init__(self,
                 xknx,
                 group_address=None,
                 group_address_state=None,
                 device_name=None,
                 after_update_cb=None,
                 setpoint_shift_step=0.5):
        """Initialize RemoteValueSetpointShift class."""
        # pylint: disable=too-many-arguments
        super().__init__(xknx,
                         group_address,
                         group_address_state,
                         device_name=device_name,
                         after_update_cb=after_update_cb)

        self.setpoint_shift_step = setpoint_shift_step

    def to_knx(self, value):
        """Convert value to payload."""
        converted_value = int(value / self.setpoint_shift_step)
        return super().to_knx(converted_value)

    def from_knx(self, payload):
        """Convert current payload to value."""
        converted_payload = super().from_knx(payload)
        return converted_payload * self.setpoint_shift_step
