import streamlit as st
import streamlit.components.v1 as components

def report():
    t1, t2 = st.columns((0.15, 1))

    t1.image("assets/logo.png", width=120)
    t2.title("CS3244 Brain Tumor - Report")

    # Using Markdown for sections
    st.markdown("""
    ## 1. Abstract
    Brain tumors are one of the leading causes of death amongst cancer types. As technologies develop and newer methods of treatment are more readily available, we must acknowledge that the first step of any process of treatment is recognition of the condition. Magnetic resonance imaging (MRI) is one of the methods to recognise brain tumors. However, traditional methods often involve manual analysis which is time and labor intensive. This project aims to alleviate these problems by automating the recognition of the presence of brain tumors through the use of machine learning models, decreasing time and manpower taken to scrutinize the MRIs.

    ## 2. Introduction
    ### 2.1: Dataset Description
    We obtained our Brain Tumor MRI Dataset from Kaggle ([Brain Tumor MRI Dataset](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)). The dataset contains images of human brain MRI images which are classified into 4 classes: glioma, meningioma, pituitary and no tumor.

    ## 3. Proposed Methodology
    Overview of our pre-processing → feature extraction → feature selection → ML models → hyperparameter tuning → analysis

    ## 4. Preprocessing
    ### 4.1: Binary Classification
    We decided to focus on binary classification to serve as a foundational step towards understanding the complexities of the dataset before scaling up to handle multiple classes in the future.

    ### 4.2: Data Splitting
    We split the dataset into 80% training and 20% testing.

    ## 5. Feature Engineering

    ### 5.1: Feature Extraction
    In the development of our machine learning model, we incorporated a robust set of features. These features were selected as they encompassed a variety of aspects critical to the differentiation of the presence of a tumor.

    ### 5.2: Feature Selection
    Our first approach was to select features based on their importance as well as filtering out features that are highly correlated. We used a Random Forest Classifier to evaluate the importance of each feature in the dataset.
    """, unsafe_allow_html=True)

    # For parts where you need HTML for better formatting

    # Adjusting the dictionary to include the category explicitly
    feature_definitions = [
        {"Feature Name": "Area", "Category": "Shape", "Definition": "Total area covered by the brain in the image, taken as the sum of all pixels in the brain’s contour."},
        {"Feature Name": "Perimeter/Area Ratio", "Category": "Shape", "Definition": "Calculated as the brain’s contour perimeter divided by the total area."},
        {"Feature Name": "Solidity", "Category": "Shape", "Definition": "Ratio of the brain’s area to its convex hull area, indicating how much of the shape is filled against how much it could potentially be filled."},
        {"Feature Name": "Circularity", "Category": "Shape", "Definition": "Measure of how close the shape is to a perfect circle, computed from the brain’s area and perimeter."},
    ]

    with st.expander("Click to view features' definitions:"):
        table = "Feature Name | Category | Definition\n---|---|---\n"
        for item in feature_definitions:
            table += f"**{item['Feature Name']}** | {item['Category']} | {item['Definition']}\n"
        st.markdown(table)


    # components.html("""
    # <style>
    # .table {
    #     font-family: Arial, sans-serif;
    #     border-collapse: collapse;
    #     width: 100%;
    # }
    # .td, .th {
    #     border: 1px solid #dddddd;
    #     text-align: left;
    #     padding: 8px;
    # }
    # .tr:nth-child(even) {
    #     background-color: #dddddd;
    # }
    # </style>
    # <table class="table">
    # <tr class="tr">
    #     <th class="th">Term</th>
    #     <th class="th">Category</th>
    #     <th class="th">Definition</th>
    # </tr>
    # <tr class="tr">
    #     <td class="td">Area</td>
    #     <td class="td">Shape Features</td>
    #     <td class="td">Total area covered by the brain in the image, taken as the sum of all pixels in the brain’s contour.</td>
    # </tr>
    # <!-- Add more rows here -->
    # </table>
    # """, height=600)

    # You can continue to add more sections of your report using t2.markdown or components.html as needed.
