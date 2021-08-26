from sklearn.metrics import confusion_matrix
# def get_model_res(y_test, res_y,prob_test):
def get_model_res(y_test, res_y):
    tn, fp, fn, tp = confusion_matrix(y_test, res_y).ravel()
    sen = tp/(tp+fn)
    diver = tn/(tn+fp)
    corre = (tp+tn)/(tp+tn+fn+fp)
    ppv = tp/(tp+fp)
    npv = tn/(fn+tn)
    y_index = sen + diver - 1
    f1 = 2*sen*ppv/(sen + ppv)
    #br = np.sum(np.square(y_test - prob_test))/len(prob_test)
    res_df = pd.DataFrame({'TRUE_NEGATIVE':[tn], 'FALSE_POSTIVE':[fp], 'FALSE_NEGATIVE':[fn], 'TRUE_POSTIVE':[tp], 'SENSITIVITY':[sen], 'DIVERSITY':[diver], 'CORRECT':[corre], 'PPV':[ppv], 'NPV':[npv], 'Youden_index':[y_index], 'F1':[f1]})
    #'br' = br
    return res_df
