if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    not_found = []
    try:
        import pandas
        print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
    except ImportError:
        print("[Missing] pandas needs to be installed")
        not_found += ["pandas"]

    try:
        import numpy
        print(f"[OK] numpy ({numpy.__version__}) - numerical computing ready")
    except ImportError:
        print("[Missing] numpy needs to be installed")
        not_found += [numpy]

    try:
        import matplotlib
        print(f"[OK] matplotlib ({matplotlib.__version__}) "
              "- Visualization ready\n")
        import matplotlib.pyplot as plot
    except ImportError:
        print("[Missing] matplotlib needs to be installed")
        not_found += ["matplotlib"]

    if not_found:
        print(f"\nMissing dependencies: {not_found}")
        print(" - Install using pip:\n   pip install -r requirements.txt")
        print(" - Or install using poetry:\n   poetry install")
        exit(1)

    print("\nAnalyzing Matrix data...")

    normal = numpy.random.normal(loc=50, scale=5, size=950)
    anomaly = numpy.random.normal(loc=90, scale=3, size=50)

    normal_df = pandas.DataFrame({
        'value': normal,
        'is_anomaly': False
    })

    anomaly_df = pandas.DataFrame({
        'value': anomaly,
        'is_anomaly': True
    })

    df = pandas.concat([normal_df, anomaly_df]).sample(frac=1)\
        .reset_index(drop=True)

    normal_points = df[~df['is_anomaly']]
    anomaly_points = df[df['is_anomaly']]

    plot.figure(figsize=(12, 6))
    # plot.show()
