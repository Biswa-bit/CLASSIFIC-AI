"""
==============================================================
CLASSIFIC-AI

Profiling Recommendation Engine

--------------------------------------------------------------
Purpose

    Generates intelligent preprocessing recommendations
    using outputs from all profiling modules.

Recommendations

    • Data Cleaning
    • Missing Value Handling
    • Encoding Strategy
    • Scaling Strategy
    • Outlier Treatment
    • Correlation Handling
    • Distribution Improvement
    • Feature Engineering
    • Dataset Readiness Score
    • Human Approval

Author : Biswadip Choudhury
Version: 1.0.0
==============================================================
"""

import pandas as pd


class ProfilingRecommendation:

    def analyze(
        self,
        df: pd.DataFrame,
        overview_result,
        column_result,
        statistics_result,
        feature_result,
        distribution_result,
        correlation_result,
        outlier_result
    ):

        recommendations = []

        readiness_score = 100

        human_approval = False

        ##########################################################
        # Recommendation Sections
        ##########################################################

        cleaning_recommendations = []

        missing_recommendations = []

        encoding_recommendations = []

        scaling_recommendations = []

        outlier_recommendations = []

        correlation_recommendations = []

        distribution_recommendations = []

        feature_engineering = []

        model_specific = []

        ##########################################################
        # Data Cleaning Rules
        ##########################################################

        total_duplicates = overview_result.get("duplicate_rows", 0)

        if total_duplicates > 0:

            cleaning_recommendations.append(
                f"Remove {total_duplicates} duplicate rows."
            )

            recommendations.append(
                f"Dataset contains {total_duplicates} duplicate rows."
            )

            readiness_score -= 5

        else:

            cleaning_recommendations.append(
                "No duplicate rows detected."
            )

        ##########################################################
        # Missing Value Rules
        ##########################################################

        total_missing = overview_result.get("missing_values", 0)

        if total_missing > 0:

            missing_recommendations.append(
                "Impute missing numeric values using Median."
            )

            missing_recommendations.append(
                "Impute categorical values using Mode."
            )

            recommendations.append(
                "Missing values detected."
            )

            readiness_score -= 10

        else:

            missing_recommendations.append(
                "No missing values detected."
            )

        ##########################################################
        # Encoding Rules
        ##########################################################

        high_cardinality = feature_result.get(
            "high_cardinality_columns",
            []
        )

        if len(high_cardinality) > 0:

            encoding_recommendations.append(
                "Use Frequency Encoding or Target Encoding "
                "for high-cardinality features."
            )

            recommendations.append(
                "High-cardinality categorical columns detected."
            )

            readiness_score -= 5

        else:

            encoding_recommendations.append(
                "Standard One-Hot Encoding is sufficient."
            )

        ##########################################################
        # Scaling Rules
        ##########################################################

        scaling_recommendations.append(
            "Scaling is recommended for Logistic Regression."
        )

        scaling_recommendations.append(
            "Scaling is recommended for SVM."
        )

        scaling_recommendations.append(
            "Scaling is recommended for KNN."
        )

        scaling_recommendations.append(
            "Scaling is recommended for Neural Networks."
        )

        scaling_recommendations.append(
            "Scaling is NOT required for Decision Trees."
        )

        scaling_recommendations.append(
            "Scaling is NOT required for Random Forest."
        )

        scaling_recommendations.append(
            "Scaling is NOT required for Extra Trees."
        )

        scaling_recommendations.append(
            "Scaling is NOT required for XGBoost."
        )

        scaling_recommendations.append(
            "Scaling is NOT required for LightGBM."
        )

        scaling_recommendations.append(
            "Scaling is NOT required for CatBoost."
        )

        ##########################################################
        # Outlier Rules
        ##########################################################

        for item in outlier_result.get("outliers", []):

            if item["severity"] != "Low":

                outlier_recommendations.append(

                    f"{item['column_name']} has {item['severity']} outliers. "
                    f"{item['recommendation']}"

                )

                readiness_score -= 3

        if len(outlier_recommendations) == 0:

            outlier_recommendations.append(

                "No significant outliers detected."

            )

        ##########################################################
        # Correlation Rules
        ##########################################################

        for item in correlation_result.get("correlation", []):

            if item["strength"] in ["Very Strong", "Strong"]:

                correlation_recommendations.append(

                    f"{item['feature_1']} ↔ {item['feature_2']} "
                    f"({item['correlation']}) : "
                    f"{item['recommendation']}"

                )

                readiness_score -= 2

        if len(correlation_recommendations) == 0:

            correlation_recommendations.append(

                "No significant multicollinearity detected."

            )

        ##########################################################
        # Distribution Rules
        ##########################################################

        for item in distribution_result.get("distribution", []):

            if item["distribution_health"] in [

                "Needs Review",

                "Poor"

            ]:

                distribution_recommendations.append(

                    f"{item['column_name']} : "
                    f"{item['recommendation']}"

                )

                readiness_score -= 2

        if len(distribution_recommendations) == 0:

            distribution_recommendations.append(

                "Feature distributions look healthy."

            )

        ##########################################################
        # Feature Engineering Suggestions
        ##########################################################

        feature_engineering.append(

            "Consider Feature Selection for high-dimensional datasets."

        )

        feature_engineering.append(

            "Consider PCA when strong multicollinearity exists."

        )

        feature_engineering.append(

            "Create interaction features where appropriate."

        )

        feature_engineering.append(

            "Engineer domain-specific business features."

        )

        ##########################################################
        # Human Approval Logic
        ##########################################################

        if readiness_score < 85:

            human_approval = True

        ##########################################################
        # Dataset Readiness
        ##########################################################

        if readiness_score >= 95:

            readiness = "Excellent"

        elif readiness_score >= 85:

            readiness = "Good"

        elif readiness_score >= 70:

            readiness = "Fair"

        else:

            readiness = "Poor"

        ##########################################################
        # Recommendation Report
        ##########################################################

        print()

        print("=" * 70)
        print("PROFILING RECOMMENDATION ENGINE")
        print("=" * 70)

        print()

        print("DATA CLEANING")
        print("-" * 70)

        for item in cleaning_recommendations:

            print(f"• {item}")

        print()

        print("MISSING VALUE RECOMMENDATIONS")
        print("-" * 70)

        for item in missing_recommendations:

            print(f"• {item}")

        print()

        print("ENCODING RECOMMENDATIONS")
        print("-" * 70)

        for item in encoding_recommendations:

            print(f"• {item}")

        print()

        print("SCALING RECOMMENDATIONS")
        print("-" * 70)

        for item in scaling_recommendations:

            print(f"• {item}")

        print()

        print("OUTLIER RECOMMENDATIONS")
        print("-" * 70)

        for item in outlier_recommendations:

            print(f"• {item}")

        print()

        print("CORRELATION RECOMMENDATIONS")
        print("-" * 70)

        for item in correlation_recommendations:

            print(f"• {item}")

        print()

        print("DISTRIBUTION RECOMMENDATIONS")
        print("-" * 70)

        for item in distribution_recommendations:

            print(f"• {item}")

        print()

        print("FEATURE ENGINEERING SUGGESTIONS")
        print("-" * 70)

        for item in feature_engineering:

            print(f"• {item}")

        print()

        print("MODEL SPECIFIC RECOMMENDATIONS")
        print("-" * 70)

        if model_specific:

            for item in model_specific:

                print(f"• {item}")

        else:

            print("• Model-specific recommendations will be generated after model selection.")

        print()

        print("OVERALL DATASET READINESS")
        print("-" * 70)

        print(f"Readiness Score     : {readiness_score}/100")

        print(f"Readiness Status    : {readiness}")

        print(f"Human Approval      : {human_approval}")

        print()

        print("=" * 70)
        print("PROFILING RECOMMENDATION ENGINE COMPLETED")
        print("=" * 70)

        ##########################################################
        # Return Results
        ##########################################################

        return {

            "module": "Profiling Recommendation Engine",

            "status": "Completed",

            "cleaning_recommendations": cleaning_recommendations,

            "missing_recommendations": missing_recommendations,

            "encoding_recommendations": encoding_recommendations,

            "scaling_recommendations": scaling_recommendations,

            "outlier_recommendations": outlier_recommendations,

            "correlation_recommendations": correlation_recommendations,

            "distribution_recommendations": distribution_recommendations,

            "feature_engineering": feature_engineering,

            "overall_recommendations": recommendations,

            "readiness_score": readiness_score,

            "readiness_status": readiness,

            "human_approval_required": human_approval

        }