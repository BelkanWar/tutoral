# heat sheet: 該選擇什麼演算法

## 統計演算法
### 如果x是類別變數，y是連續變數
* 你只有兩個群
    * 各類別的y符合常態分佈: `t-test`
    * 否則: `Mann-Whitney U test`
* 超過兩個群
    * 各類別的y符合常態分佈: `ANOVA`
    * 否則: `Kruskal-Wallis test`

* 常態分佈檢定: `shapiro test`
* 標準差檢定: `Bartlett test`, `Fligner-Killeen test`

### 如果x和y都是類別變數
* Chi-square goodness of fit  
* Fisher exact test

### 如果y是連續變數, X含有連續變數, 而且y和x是線性關係
* simple linear regression model

### 如果y是計次變數, X含有連續變數, 而且y和x是線性關係
* 資料的variance和mean沒有顯著差異
    *  Poisson regression model
* 否則
    * Negative binomial regression model

### 如果y是二元資料, x含有連續變數, 而且y和x是線性關係
* logistic regression model

## 機器學習演算法
### 如果y是類別變數
* Naive bayes model
* SVM
* Tree-based algorithm
    * Random forest
    * gradient boosting, like `XGBoost-classifier`

### 如果y是連續變數
* XGBoost-
* LOESS
* Generalized-additive model

### 如果沒有y
* 特徵抽取: `PCA`
* 分群: `cluster analysis`

### 如果問題太複雜, 而且資料集超大
* 神經網路