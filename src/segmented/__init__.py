from dataclasses import dataclass


@dataclass
class SegmentedUser:
    name: str
    roles: tuple[str]


def user_has_permissions(self, user: SegmentedUser, requested_permission: str):
    for role in user.roles:
        if role in (self.permissions.get(requested_permission.lower()) or []):
            return True
    return False


def apply_permissions(**kwargs):
    def inner(cls):
        cls.user_has_permissions = user_has_permissions
        # Make all the permissions lowercase, to normalize the case used in getting permissions
        cls.permissions = {k.lower(): v for k, v in kwargs.items()}
        return cls

    return inner
