import numpy as np


def histogram_equalization(channel):
    """
    Apply histogram equalization to the given channel.
    """
    hist, _ = np.histogram(channel.flatten(), 256, [0, 1])
    cdf = hist.cumsum()
    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')
    return cdf[(channel * 255).astype(np.uint8)]


def merge_channels(red=None, green=None, blue=None, red_intensity=1.0, green_intensity=1.0, blue_intensity=1.0, equalize=True):
    """
    Merge specified Red, Green, and Blue channels into a single image or 3D volume. 
    Intensity of each channel can be adjusted. If specified, histogram equalization is applied to each channel.
    The merged output is rescaled to utilize the full [0, 1] dynamic range.

    Args:
        red, green, blue (numpy.ndarray): 2D or 3D arrays representing the Red, Green, and Blue channels, respectively.
        red_intensity, green_intensity, blue_intensity (float): Scalars in the range [0, 1] to adjust the intensity of each channel.
        equalize (bool): If True, applies histogram equalization to each channel.

    Returns:
        numpy.ndarray: A merged and rescaled multi-channel (RGB) 2D image or 3D volume.

    Raises:
        ValueError: If intensity values are not in the [0, 1] range, or if no channels are provided.
    """
    
    # Validate intensity values
    for intensity in (red_intensity, green_intensity, blue_intensity):
        if not 0 <= intensity <= 1:
            raise ValueError("Intensities should be in the range [0, 1].")

    # Determine the shape based on provided channels
    shape = None
    for channel in (red, green, blue):
        if channel is not None:
            if shape is not None and shape != channel.shape:
                raise ValueError("All provided channels must have the same shape.")
            shape = channel.shape

    # If no channels are provided, raise an error
    if shape is None:
        raise ValueError("At least one channel should be provided.")

    # Function to adjust channel intensity and apply equalization if needed
    def get_adjusted_channel_or_zeros(channel, intensity):
        if channel is None:
            return np.zeros(shape, dtype=np.float32)
        adjusted_channel = channel * intensity
        return histogram_equalization(adjusted_channel) if equalize else adjusted_channel

    # Adjust intensities and equalize if needed
    red = get_adjusted_channel_or_zeros(red, red_intensity)
    green = get_adjusted_channel_or_zeros(green, green_intensity)
    blue = get_adjusted_channel_or_zeros(blue, blue_intensity)

    # Stack and rescale
    merged = np.stack([red, green, blue], axis=-1)
    min_val, max_val = merged.min(), merged.max()
    merged = (merged - min_val) / (max_val - min_val) if max_val > min_val else merged

    return merged