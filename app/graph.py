from altair import Chart


def chart(df, x, y, target) -> Chart:
    return Chart(df).mark_circle(size=60).encode(
        x=x,
        y=y,
        color=target
    )
