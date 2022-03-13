report_fp.write('classification report of train data:\n')
report_fp.write(classification_report(y_true = y_train_true, y_pred = y_train_pred,
target_names = class_name)+'\n\n')
report_fp.write('classification report of val data:\n')
report_fp.write(classification_report(y_true = y_val_true, y_pred = y_val_pred,
target_names = class_name)+'\n\n') 