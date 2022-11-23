from src.kafka_producer.json_producer import product_data_using_file
from src.constant import SAMPLE_DIR
import os
if __name__ == '__main__':
    
    topics = os.listdir(SAMPLE_DIR)
    
    topics.remove(".DS_Store")
    
    print(f'topics: [{topics}]')
    #topics=list(topics[1])
    for topic in topics:
        print(topic)
        sample_topic_data_dir = os.path.join(SAMPLE_DIR,topic)
        print(sample_topic_data_dir)
        sample_file_path = os.path.join(sample_topic_data_dir,os.listdir(sample_topic_data_dir)[0])
        product_data_using_file(topic=topic,file_path=sample_file_path)

