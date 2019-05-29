import tensorflow as tf
# 初始化结构
a = tf.Variable(tf.zeros(1))
a = tf.assign_add(a,tf.ones(1))
sum = 0.0

# b_vaulue = tf.add(a,b)
# 创建一个sess对话
sess = tf.Session()
# 运行一个sess对话
sess.run(tf.global_variables_initializer())

for i in range(10):
    c = sess.run(a)
    sum = sum+c
print((sum))

# a = 0.0
# b = tf.add(a,1)
# 使用变量的时候要注意的是变量I中的变化过程
# a=tf.rang(1,11)