def declare_winner(report_a, report_b):

    if report_a["mean_score"] > report_b["mean_score"]:

        return "Config A"

    if report_b["mean_score"] > report_a["mean_score"]:

        return "Config B"

    return "Tie"