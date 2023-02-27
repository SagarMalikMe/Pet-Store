import CategoryCard from '../components/CategoryCard';
import styles from '../styles/Home.module.css';
  
const HomePage = () => {
  return (
      <main className={styles.container}>
        <div className={styles.large}>
          <CategoryCard image="https://imgur.com/PUTcxwn.jpeg" name="Dog" />
          <CategoryCard image="https://imgur.com/apq9rcW.jpeg" name="Birds" />
          
        </div>
        <div className={styles.large}>
          <CategoryCard image="https://imgur.com/li2guyj.jpeg" name="Fish" />
          <CategoryCard
            image="https://imgur.com/9PxgtfR.jpeg"
            name="Food"
          />
        </div>
      </main>
    );
  };
  
export default HomePage;
  



