java -cp "%CLASSPATH%;C:\Program Files\Weka-3-8\weka.jar;C:\Program Files\Weka-3-8\mysql-connector-java-5.0.5-bin.jar" weka.classifiers.meta.CostSensitiveClassifier -cost-matrix "[0.0 1.0; 1.0 0.0]" -S 1 -W weka.classifiers.functions.Logistic -- -R 1.0E-8 -M -1 -num-decimal-places 4 -t "C:\Users\hlope\Desktop\GitHub\PHD\CAP 6673 Data Mining & Mach Learning\Assignment5\fit.arff" -T "C:\Users\hlope\Desktop\GitHub\PHD\CAP 6673 Data Mining & Mach Learning\Assignment5\test.arff" -d ./model.arff


java -cp "%CLASSPATH
%;C:/Program Files/Weka-3-8/weka.jar;C:/Program Files/Weka-3-8/mysql-connector-java-5.0.5-bin.jar" weka.classifiers.functions.Logistic -t "C:/Users/hlope/Desktop/GitHub/PHD/CAP 6673 Data Mining & Mach Learning/Assignment5/fit.arff" -d "C:/Users/hlope/Desktop/GitHub/PHD/CAP 6673 Data Mining & Mach Learning/Assignment5/model.arff"


weka.classifiers.meta.CostSensitiveClassifier -cost-matrix "[0.0 1.0; 1.0 0.0]" -S 1 -W weka.classifiers.functions.Logistic -- -R 1.0E-8 -M -1 -num-decimal-places 4



Command line to generate model output :

java -cp "%CLASSPATH
%;C:/Program Files/Weka-3-8/weka.jar;"  weka.classifiers.meta.CostSensitiveClassifier -cost-matrix "[0.0 1.0; 1.0 0.0]" -S 1 -W weka.classifiers.functions.Logistic -t "C:/Users/hlope/Desktop/GitHub/PHD/CAP 6673 Data Mining & Mach Learning/Assignment5/fit.arff" -c 1 > model.txt


Python script that can generate all the permutations :

local_path = "C:/Users/hlope/Desktop/GitHub/PHD/CAP 6673 Data Mining & Mach Learning/Assignment5/"

fit_path = local_path + "/fit.arff";
test_path= local_path + "/test.arff";

for(int i =0.1 ; i <2.0 ; i+ 0.2){
cv_output = local_path + string("/cv_logit_model_cost_{0}.txt",c);
test_output = local_path + string("/tst_logit_model_cost_{0}.txt",c);

    c = i;

    cv_model_cmd = string("java -cp '%CLASSPATH
    %;C:/Program Files/Weka-3-8/weka.jar;'  weka.classifiers.meta.CostSensitiveClassifier -cost-matrix "[0.0 1.0; {0} 0.0]" -S 1 -W weka.classifiers.functions.Logistic -t {1} -c 1 > {2}",c, fit_path,cv_output)

    t_model_cmd = string("java -cp '%CLASSPATH
    %;C:/Program Files/Weka-3-8/weka.jar;'  weka.classifiers.meta.CostSensitiveClassifier -cost-matrix "[0.0 1.0; {0} 0.0]" -S 1 -W weka.classifiers.functions.Logistic -t {1} -T {2} -c 1 > {3}",c, fit_path,test_path,test_output)

//parse output files into dataframes
//use it to create confusion matrix
}
