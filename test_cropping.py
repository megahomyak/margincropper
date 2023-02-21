import pytest
from margincropper import crop_margins, ContentNotFound
from PIL import Image


def repeat(n):
    return (n, n, n)


def test_cropping_an_image_consisting_or_margins():
    image = Image.frombytes("RGB", (3, 3), bytes([
        128, 130, 133, 128, 125, 128, 127, 131, 132,
        126, 128, 133, 124, 127, 132, 124, 125, 131,
        125, 127, 128, 124, 126, 134, 123, 127, 128,
    ]))
    with pytest.raises(ContentNotFound):
        crop_margins(image, (125, 128, 131), 3)


def test_cropping_an_image_with_content():
    image = Image.frombytes("RGB", (3, 3), bytes([
        128, 130, 133, 128, 125, 128, 127, 131, 132,
        126, 128, 133, 124, 000, 132, 124, 125, 131,
        125, 127, 128, 124, 126, 134, 123, 127, 128,
    ]))
    print(list(crop_margins(image, (125, 128, 131), 3).getdata()))
    assert crop_margins(image, (125, 128, 131), 3) == Image.frombytes("RGB", (1, 1), bytes([
        124, 000, 132,
    ]))
