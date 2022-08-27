from segmented import *
from flask import Flask

app = Flask(__name__)


@dataclass
@apply_permissions(
    read=(
        "User",
        "Admin"
    ),
    write=(
        "Admin",
    )
)
class TestDataClass:
    x: int


sally = TestDataClass(x=10)

bob = SegmentedUser(
    "bob",
    (
        "User",
    )
)

admin = SegmentedUser(
    "admin",
    (
        "Admin",
    )
)

if sally.user_has_permissions(admin, "Read"):
    print(sally.x)
if sally.user_has_permissions(admin, "Write"):
    sally.x = 100
if sally.user_has_permissions(bob, "Read"):
    print(sally.x)
