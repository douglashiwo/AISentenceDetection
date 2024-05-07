# AISentenceDetection(IJCAI 2024 full paper on the Special Track of AI and Social Good )


1.These are the implemented codes for our IJCAI 2024 accpeted paper (https://arxiv.org/abs/2403.03506).

2.For details about this paper.Please refer to our paper:

      **Detecting AI-Generated Sentences in Realistic Human-AI Collaborative Hybrid Texts: Challenges, Strategies, and Insights**
      BibTex:

      @article{zeng2024detecting,
            title={Detecting AI-Generated Sentences in Realistic Human-AI Collaborative Hybrid Texts: Challenges, Strategies, and Insights}, 
            author={Zijie Zeng and Shiqi Liu and Lele Sha and Zhuang Li and Kaixun Yang and Sannyuya Liu and Dragan Gašević and Guanliang Chen},
            year={2024},
            journal={Proceedings of the 33rd International Joint Conference on Artificial Intelligence}
          
      }

Dir A-Segment_Detection_Models contains all the segment detection models which detect segments by locating the boundaries between sentences of different authorship, .e.g., between human-written sentences and AI-written sentence.

Dir B-Segment_Classification_Models contains all the segment classification models which can perform classification over inputs such as a single sentence or a segment of several sentences. 

----------------------------------------------------------------------------------

Although we follow the pipeline of segment detection followed by segment classification to address sentence-level AI-content detection from hybrid texts, the segment detection task and sentence (not segment) classification task can actually be performed simultaneously.

For example, for an essay containing five sentences ⟨s1​,s2​,s3​,s4​,s5​⟩, we can predict a label for each sentence using the segment classification model (treating each sentence as a segment). Let's say the prediction is <human,human,human,human,AI-written>. At the same time, we can apply the segment detection model to detect possible segments from ⟨s1​,s2​,s3​,s4​,s5​⟩. Let's say two segments have been detected: ⟨s1​,s2​⟩ and ⟨s3​,s4​,s5​⟩.

In this case, if we choose to trust the prediction of the segment detection model, then we should change the prediction of the last sentence (s5​) from 'AI-written' to 'human-written' because the segmentation model believes that s3​,s4​,s5​ should share the same label (i.e., segment classification based on sentence prediction results and the segment detection results).


