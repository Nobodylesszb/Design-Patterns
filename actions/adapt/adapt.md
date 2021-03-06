### 适配器模式
**定义**
- 适配器模式定义如下：将一个类的接口变换成客户端期待的另一种接口，从而使原本因接口不匹配而无法在一起工作的两个类能够在一起工作。适配器模式和装饰模式有一定的相似性，都起包装的作用，但二者本质上又是不同的，装饰模式的结果，是给一个对象增加了一些额外的职责，而适配器模式，则是将另一个对象进行了“伪装”。
- 适配器可以认为是对现在业务的补偿式应用，所以，尽量不要在设计阶段使用适配器模式，在两个系统需要兼容时可以考虑使用适配器模式。

#### 适配器模式的优点和使用场景
**优点**
1. 适配器模式可以让两个接口不同，甚至关系不大的两个类一起运行；
2. 提高了类的复用度，经过“伪装”的类，可以充当新的角色；
3. 适配器可以灵活“拆卸”。

**应用场景:**
1. 不修改现有接口，同时也要使该接口适用或兼容新场景业务中，适合使用适配器模式。例如，在一个嵌入式系统中，原本要将数据从Flash读入，现在需要将数据从磁盘读入，这种情况可以使用适配器模式，将从磁盘读入数据的接口进行“伪装”，以从Flash中读数据的接口形式，从磁盘读入数据。

#### 适配器模式的缺点
1. 适配器模式与原配接口相比，毕竟增加了一层调用关系，所以，在设计系统时，不要使用适配器模式。