#!/usr/bin/env python
import argparse
import logging

# Logging module is used to track events that have occured and alert the user.
# logging is much more powerful and configurable when working on production ready code.
logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    # since we put level=logging.INFO in the config,
    # the following message will NOT be printed. It will be 
    # printed if we change =logging.DEBUG
    logger.debug("This is a debug message")
    # Mark the message as "info" importance
    logger.info("This is a message")
    # Mark the message as "warning" importance
    logger.warning("This is a warning")
    # Mark the message as "error" importance
    logger.error("This is an error")

    logger.info(f"This is {args.artifact_name}")

    logger.info(f"This is {args.optional_arg}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="This is a tutorial on argparse"
    )

    parser.add_argument(
        "--artifact_name", type=str, help="Name and version of W&B artifact", required=True
    )

    parser.add_argument(
        "--optional_arg", type=float, help="An optional argument", required=False,
        default=2.3
    )

    args = parser.parse_args()

    go(args)
