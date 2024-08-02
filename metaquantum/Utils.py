import os
import pickle
import torch

class Saving:
    @staticmethod
    def save_test():
        # 這是一個示範函數，根據實際需求進行實現
        print("Saving test data...")
    
    @staticmethod
    def save_training_and_testing(exp_name, file_title, training_x, training_y, val_x, val_y, testing_x, testing_y):
        # 創建保存目錄
        if not os.path.exists(exp_name):
            os.makedirs(exp_name)
        
        # 保存訓練數據
        with open(os.path.join(exp_name, file_title + '_train.pkl'), 'wb') as f:
            pickle.dump((training_x, training_y), f)
        
        # 保存驗證數據
        with open(os.path.join(exp_name, file_title + '_val.pkl'), 'wb') as f:
            pickle.dump((val_x, val_y), f)
        
        # 保存測試數據
        with open(os.path.join(exp_name, file_title + '_test.pkl'), 'wb') as f:
            pickle.dump((testing_x, testing_y), f)

    @staticmethod
    def save_all_the_current_info(exp_name, file_title, iter_index, var_Q_circuit, var_Q_bias, cost_train_list, cost_test_list, acc_train_list, acc_val_list, acc_test_list):
        # 創建保存目錄
        if not os.path.exists(exp_name):
            os.makedirs(exp_name)
        
        # 保存訓練資訊
        with open(os.path.join(exp_name, file_title + '_info.pkl'), 'wb') as f:
            pickle.dump({
                'iter_index': iter_index,
                'var_Q_circuit': var_Q_circuit,
                'var_Q_bias': var_Q_bias,
                'cost_train_list': cost_train_list,
                'cost_test_list': cost_test_list,
                'acc_train_list': acc_train_list,
                'acc_val_list': acc_val_list,
                'acc_test_list': acc_test_list
            }, f)

    @staticmethod
    def saving_torch_model(exp_name, file_title, iter_index, model_state_dict):
        # 創建保存目錄
        if not os.path.exists(exp_name):
            os.makedirs(exp_name)
        
        # 保存模型
        torch.save({
            'iter_index': iter_index,
            'model_state_dict': model_state_dict
        }, os.path.join(exp_name, file_title + '_model.pth'))

# 你可以在這裡添加更多的實用函數
