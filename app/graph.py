from altair import Chart


def chart(df, x, y, target) -> Chart:
    props = {
        'background': '#000000',
        'width': 600,
        'height': 600,
        'padding': 30
    }
    configs = {
        'title': {
            'color': '#FFFFFF',
            'fontSize': 30,
            'offset': 30,
        },
        'legend': {
            'titleFontSize': 20,
            'titleColor': '#FFFFFF',
            'labelColor': '#FFFFFF',
            'labelFontSize': 15,
        },
        'axis': {
            'labelPadding': 10,
            'labelFontSize': 15,
            'labelColor': '#FFFFFF',
            'titlePadding': 15,
            'titleFontSize': 20,
            'titleColor': '#FFFFFF',
            'gridColor': '#FFFFFF',
            'tickColor': '#FFFFFF',
            'tickSize': 5,
        },
    }

    visual = Chart(
        df,
        title=f"{y} by {x} for {target}",
    ).mark_circle(size=75).encode(
        x=x,
        y=y,
        color=target
    ).properties(**props).configure(**configs)

    return visual
