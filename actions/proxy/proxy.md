### 代理模式
**代理模式定义如下**：
- 为某对象提供一个代理，以控制对此对象的访问和控制。代理模式在使用过程中，应尽量对抽象主题类进行代理，而尽量不要对加过修饰和方法的子类代理。如上例中，如果有一个xServer继承了Server，并新加了方法xMethod，xServer的代理应以Server为主题进行设计，而尽量不要以xServer为主题，以xServer为主题的代理可以从ServerProxy继承并添加对应的方法。
- 在JAVA中，讲到代理模式，不得不会提到动态代理。动态代理是实现AOP（面向切面编程）的重要实现手段。而在Python中，很少会提到动态代理，而AOP则会以另一种模式实现：装饰模式。有关AOP的相关内容，我们会在装饰模式这一节中进行说明。

#### 代理模式的优点和应用场景
**优点:**
  1. 职责清晰：非常符合单一职责原则，主题对象实现真实业务逻辑，而非本职责的事务，交由代理完成；
  2. 扩展性强：面对主题对象可能会有的改变，代理模式在不改变对外接口的情况下，可以实现最大程度的扩展；
  3. 保证主题对象的处理逻辑：代理可以通过检查参数的方式，保证主题对象的处理逻辑输入在理想范围内。

**应用场景:**

  1. 针对某特定对象进行功能和增强性扩展。如IP防火墙、远程访问代理等技术的应用；
  2. 对主题对象进行保护。如大流量代理，安全代理等；
  3. 减轻主题对象负载。如权限代理等。

**缺点:**
  1. 可能会降低整体业务的处理效率和速度
   