"""
==========================================================
CLASSIFIC-AI

Dataset Approval Gate
==========================================================
"""


class DatasetApproval:

    def build(self, readiness):

        ####################################################
        # Automatic Decision
        ####################################################

        if readiness["score"] >= 90:

            status = "APPROVED"

            human_approval = False

            message = (
                "Dataset approved automatically."
            )

        elif readiness["score"] >= 70:

            status = "REVIEW"

            human_approval = True

            message = (
                "Review recommended before continuing."
            )

        else:

            status = "REJECTED"

            human_approval = True

            message = (
                "Dataset not ready for preprocessing."
            )

        ####################################################
        # Return
        ####################################################

        return {

            "status": status,

            "human_approval_required": human_approval,

            "message": message

        }
    