# TikTok Claims Classification

## 📌 Overview

This project is part of the **Google Advanced Data Analytics Professional Certificate** on Coursera.

The project focuses on exploring TikTok video data to identify factors associated with whether a video is classified as a **claim** or an **opinion**. The exploratory analysis provides the foundation for a future machine learning classification model.

---

## 🎯 Business Problem

The TikTok data team wants to develop a machine learning model that can classify videos as either:

- **Claims** — videos that make a claim or assertion.
- **Opinions** — videos that express an opinion.

The objective of this analysis is to identify patterns in the data that may help predict a video's claim status and understand which factors are associated with higher engagement.

---

## 📊 Dataset

The dataset contains information about **19,382 TikTok videos** across **12 variables**.

The data includes:

- Video characteristics and duration
- Claim status
- Video transcription
- Author verification and ban status
- Views
- Likes
- Shares
- Downloads
- Comments

The dataset contains missing values in several variables, particularly in claim status, transcription, and engagement metrics.

---

## 🔎 Analysis

The project focuses on **Exploratory Data Analysis (EDA)** using Python and Pandas.

The main areas investigated were:

- Distribution of claims vs. opinions
- Video engagement patterns
- Relationship between claim status and author ban status
- Engagement differences across author ban statuses
- Engagement rates relative to video views

Three engagement-rate features were also created:

- `likes_per_view`
- `comments_per_view`
- `shares_per_view`

These metrics allow engagement to be compared while accounting for differences in total video views.

---

## 📈 Key Findings

### Claim vs. Opinion

Among the **19,084 videos with a known claim status**:

- **50.35%** were classified as claims.
- **49.65%** were classified as opinions.

The two classes are therefore relatively balanced.

### Engagement

Views, likes, shares, and comments have highly skewed distributions. A relatively small number of videos receive exceptionally high engagement.

Because of this skewness, the **median is often more representative than the mean** when describing typical engagement.

### Author Status

The analysis identified differences in claim status and engagement across author ban statuses.

This suggests that `author_ban_status` may contain useful information for predicting claim status and understanding engagement behavior.

### Engagement Rates

Normalized metrics such as `likes_per_view`, `comments_per_view`, and `shares_per_view` provide additional insight into how strongly users interact with videos relative to their total number of views.

---

## 🛠️ Tools

- **Python**
- **Pandas**
- **Jupyter Notebook**
- **Exploratory Data Analysis**
- **Descriptive Statistics**
- **Feature Engineering**
