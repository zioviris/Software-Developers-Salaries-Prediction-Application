import streamlit as st
#from predict_page_2020 import show_predict_page_decision_tree, show_predict_page_linear_regression, show_predict_page_random_forest
#from predict_page_2021 import show_predict_page_decision_tree, show_predict_page_linear_regression, show_predict_page_random_forest
#from explore_page_2021 import show_explore_page
#from explore_page_2020 import show_explore_page

page = st.sidebar.selectbox("Explore Or Predict", ("Explore", "Predict"))
page2 = st.sidebar.selectbox("Year", ("2021", "2020", "2019", "2018"))

if page == "Explore":
    if page2 == "2020":
        from explore_page_2020 import show_explore_page
    elif page2 == "2021":
        from explore_page_2021 import show_explore_page
    elif page2 == "2019":
        from explore_page_2019 import show_explore_page
    elif page2 == "2018":
        from explore_page_2018 import show_explore_page
    show_explore_page()

else:
    page3 = st.sidebar.selectbox("Model", ("Linear Regression", "Random Forest", "Decision Tree"))

if page == "Predict":
    if page2 == "2021":
        from predict_page_2021 import show_predict_page_decision_tree, show_predict_page_linear_regression, show_predict_page_random_forest
    elif page2 == "2020":
        from predict_page_2020 import show_predict_page_decision_tree, show_predict_page_linear_regression, show_predict_page_random_forest
    elif page2 == "2019":
        from predict_page_2019 import show_predict_page_decision_tree, show_predict_page_linear_regression, show_predict_page_random_forest
    elif page2 == "2018":
        from predict_page_2018 import show_predict_page_decision_tree, show_predict_page_linear_regression, show_predict_page_random_forest
    if page3 == "Random Forest":
        show_predict_page_random_forest()
    elif page3 == "Decision Tree":
        show_predict_page_decision_tree()
    elif page3 == "Linear Regression":
        show_predict_page_linear_regression()



