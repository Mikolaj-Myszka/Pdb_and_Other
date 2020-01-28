import logging
import math

# print(dir(logging))

# Create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="lumberjack.log",
                    level=logging.DEBUG, 
                    format=LOG_FORMAT, 
                    filemode="w")
logger = logging.getLogger()

"""
# Test the logger
logger.debug("Debug mode.")
logger.info("Info mode.")
logger.warning("Warning mode.")
logger.error("Error mode.")
logger.critical("Critical mode.")

print(logger.level)
"""


def quadratic_formula(a, b, c):
    """Return the solution to the equation ax^2 + bx + c = 0."""
    logger.info("quadratic_formula({0}, {1}, {2})".format(a, b, c))

    # Compute the discriminant
    logger.debug("# Compute the discriminant.")
    disc = b^2 - 4*a*c

    # Compute the 2 roots
    logger.debug("# Compute the 2 roots")
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)

    # Return the roots (as a tuple)
    logger.debug("# Return the roots")
    return (root1, root2)


roots = quadratic_formula(1, 0, -4)
#roots = quadratic_formula(1, 0, 1)
print(roots)


