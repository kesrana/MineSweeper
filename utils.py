import settings

def height_prct(percentage: float)->float:
    return (settings.HEIGHT / 100) * percentage

def width_prct(percentage: float) -> float:
    return (settings.WIDTH / 100) * percentage
