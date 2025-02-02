close all
%clear all
clc
Ts = 50e-06;
Ts_Power = 50e-06;
Ts_Control = 50e-06;
R=[0.0001 0.001 0.01 1 10 50 100];
%R=[0.0001 0.001 0.01 1 5];
T=[0.05 0.05139 0.0527 0.054 0.0554 0.0568 0.0589 0.06 0.06139 0.0627 0.064 0.0654];
L=50;
for i=1:10
    R1=R(1,i);
    for L1=1:5:49
        L2=L-L1;
        for j=1:12
            T1=T(1,j);
            sim('E:\MATLAB Microgrid\project1.slx');
            import v_1.*
            import v_2.*
            import v_3.*
            import v_4.*
            import i_1.*
            import i_2.*
            import i_3.*
            import i_4.*
            t= table(v_1.data,i_1.data);
            t1= table(v_2.data,i_2.data);
            t2= table(v_3.data,i_3.data);
            t3= table(v_4.data,i_4.data);
            name="AG_1_2_"+"_R_"+num2str(R1)+"_L_"+num2str(L1)+"_T_"+num2str(T1)+".xlsx";
            writetable(t,name,'sheet',1);
            writetable(t1,name,'sheet',2);
            writetable(t2,name,'sheet',3);
            writetable(t3,name,'sheet',4);
        end
    end
end
                    
            
            
                   
            
    
