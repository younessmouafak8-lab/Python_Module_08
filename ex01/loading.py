import sys

if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    # collect missing packages to report all at once instead of
    # crashing on first missing one
    not_found = []

    # imports inside try/except to gracefully handle missing packages
    # instead of crashing with a hard ImportError
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
        not_found += ["numpy"]

    try:
        import matplotlib
        print(f"[OK] matplotlib ({matplotlib.__version__}) "
              "- Visualization ready")
        # pyplot is the plotting interface, imported separately from matplotlib
        import matplotlib.pyplot as plot
    except ImportError:
        print("[Missing] matplotlib needs to be installed")
        not_found += ["matplotlib"]

    # exit with code 1 (error) if any required package is missing
    if not_found:
        print(f"\nMissing dependencies: {not_found}")
        print(" - Install using pip:\n   pip install -r requirements.txt")
        print(" - Or install using poetry:\n   poetry install")
        sys.exit(1)

    print("\nAnalyzing Matrix data...")

    # simulate normal system activity: 950 points centered around 50
    normal = numpy.random.normal(loc=50, scale=5, size=950)
    # simulate agent intrusions: 50 anomalous points centered around 90
    anomaly = numpy.random.normal(loc=90, scale=3, size=50)

    print("Processing 1000 data points...")

    # build separate dataframes then combine them
    normal_df = pandas.DataFrame({
        'value': normal,
        'is_anomaly': False
    })
    anomaly_df = pandas.DataFrame({
        'value': anomaly,
        'is_anomaly': True
    })

    # concat merges both dataframes, sample(frac=1) shuffles all rows randomly
    # reset_index renumbers rows from 0 to 999 after shuffling
    df = (pandas.concat([normal_df, anomaly_df])
          .sample(frac=1)
          .reset_index(drop=True))

    # ~ operator negates the boolean column (pandas equivalent of 'not')
    normal_points = df[~df['is_anomaly']]
    anomaly_points = df[df['is_anomaly']]

    print("Generating visualization...")

    # 12x6 inches gives enough horizontal space for 1000 points
    plot.figure(figsize=(12, 6))

    # alpha controls transparency to avoid overlapping dots
    # forming a solid blob
    plot.scatter(normal_points.index, normal_points['value'], color="green",
                 label="Normal activity", s=10)
    plot.scatter(anomaly_points.index, anomaly_points['value'], color="red",
                 label="Abnormal activity", s=10)

    plot.title('Matrix System Activity — Agent Intrusion Detection')
    plot.xlabel('Data Point')
    plot.ylabel('Activity Level')
    # legend picks up all label= values from scatter automatically
    plot.legend()

    # savefig must come before show() — show() clears the figure from memory
    plot.savefig('matrix_analysis.png')

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")
