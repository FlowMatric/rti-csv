import pandas as pd

print("Hello World")

csvfp = "data/FlatheadCatfish_ContiguousArea_Baseline.csv"

a = pd.read_csv(csvfp, header=None, skip_blank_lines=False)
print(a)

thisIsMyNewVar: str = "Hello"

for i in range(10):
    key = a.iloc[i, 0]
    if key == "Scenario":
        test_id = None
        # Add a special log message
        value = a.iloc[i, 1]
        if "Baseline" in value:
            pass
        elif value.startswith("Test"):
            print(
                "Parsing the Test ID, We make this line more than 80 characsdfkljsdlfj  lksdjflkjsdf  ters long..."  # noqa
            )  # noqa
            for ch in value[4:]:
                try:
                    i = int(ch)
                except ValueError:
                    continue


def test_some_docstring(arg1):
    "Some invalid docstring"
    print("Well this is cool@!")
