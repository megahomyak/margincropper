# Margincropper

## Usage example

    from margincropper import crop_margins, ContentNotFound

    image_with_cropped_margins = crop_margins(image)

    try:
        crop_margins(an_image_consisting_only_of_margins)
    except ContentNotFound:  # This exception will be raised
        pass
