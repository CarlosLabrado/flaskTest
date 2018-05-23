import dbus


def python_from_dbus(obj):
    """dbus object to Python object conversion, simplified version from
    http://www.programcreek.com/python/example/13530/dbus.Boolean
    """
    if isinstance(obj, dbus.Boolean):
        python_obj = bool(obj)
    elif isinstance(object, dbus.String):
        python_obj = str(obj)
    elif isinstance(obj, (dbus.Byte,
                          dbus.Int16,
                          dbus.Int32,
                          dbus.Int64,
                          dbus.UInt16,
                          dbus.UInt32,
                          dbus.UInt64)):
        python_obj = int(obj)
    elif isinstance(obj, dbus.Double):
        python_obj = float(obj)
    else:
        raise TypeError("Unhandled %s" % obj)
    return python_obj


class DBUSCommands:
    """
    https://docs.resin.io/learn/develop/runtime/#rebooting-the-device
    """

    def __init__(self):
        self._bus = dbus.SystemBus()
        self._proxy = self._bus.get_object('org.freedesktop.systemd1',
                                           '/org/freedesktop/systemd1')
        self._interface = dbus.Interface(self._proxy, 'org.freedesktop.systemd1.Manager')
        self.status = self.reboot_device()

    def reboot_device(self):
        try:
            print("trying to reboot")
            reboot = self._interface.Reboot()
        except dbus.exceptions.DBusException as err:
            raise err

        return reboot
