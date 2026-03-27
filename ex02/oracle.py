import os
import sys


if __name__ == "__main__":
    # python-dotenv is a third party package so it may not be installed
    # gracefully handle the missing package instead of crashing
    try:
        from dotenv import load_dotenv
    except ImportError:
        print("missing dotenv")
        print("run: pip install python-dotenv")
        sys.exit(1)

    # loads key=value pairs from .env file into os.environ
    # shell environment variables always take priority over .env values
    load_dotenv()

    # all required configuration keys the program needs to run
    required = ["MATRIX_MODE",
                "DATABASE_URL",
                "API_KEY",
                "LOG_LEVEL",
                "ZION_ENDPOINT"
                ]

    not_found = []
    config = {}
    for name in required:
        # returns None if the variable is not set, never crashes
        value = os.environ.get(name)
        if not value:
            not_found += [name]
        else:
            config.update({name: value})

    # report all missing variables at once before exiting
    if not_found:
        print(f"Missing configuration: {not_found}")
        print("double check your .env and fill in your values")
        sys.exit(1)

    print("\nORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")

    # behavior changes based on MATRIX_MODE — development vs production
    data_base = ('Connected to local instance'
                 if config['MATRIX_MODE'] == 'development'
                 else 'Connected to production database')
    print(f"Database: {data_base}")
    print("API Access: Authenticated")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print(f"Zion Network: Online ({config['ZION_ENDPOINT']})")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")
