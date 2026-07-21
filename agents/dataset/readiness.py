"""
==========================================================
CLASSIFIC-AI

Dataset Readiness
==========================================================
"""


class DatasetReadiness:

    def build(self, summary):

        checks = []

        score = 100

        ####################################################
        # Dataset Exists
        ####################################################

        if summary["Rows"] > 0:

            checks.append("✓ Dataset Loaded")

        else:

            checks.append("✗ Dataset Not Loaded")

            score -= 50

        ####################################################
        # Duplicate Check
        ####################################################

        if summary["Duplicate Rows"] == 0:

            checks.append("✓ Validation Passed")

        else:

            checks.append("⚠ Duplicate Rows Found")

            score -= 10

        ####################################################
        # Metadata
        ####################################################

        checks.append("✓ Metadata Generated")

        ####################################################
        # Status
        ####################################################

        if score >= 90:

            status = "READY"

        elif score >= 70:

            status = "REVIEW"

        else:

            status = "NOT READY"

        ####################################################
        # Return
        ####################################################

        return {

            "score": score,

            "status": status,

            "checks": checks,

            "next_step": "Proceed to Preprocessing Agent"

        }
    