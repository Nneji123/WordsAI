from .app import get_sentiment
from .app import get_summary



# write test functions for the get_summary function
def test_get_summary():
    text = "The quick brown fox jumped over the lazy dog."
    result = get_summary(text)
    assert result["summary_list"] == ["The quick brown fox jumped over the lazy dog."]
    assert result["title_string"] == "The quick brown fox jumped over the lazy dog."
    assert result["abstract_string"] == "The quick brown fox jumped over the lazy dog."
    assert result["abstract_list"] == ["The quick brown fox jumped over the lazy dog."]
    assert result["abstract_score"] == 1.0
    assert result["abstract_rank"] == 1
    assert result["abstract_rank_list"] == [1]
    assert result["abstract_score_list"] == [1.0]
    assert result["abstract_sentence_list"] == ["The quick brown fox jumped over the lazy dog."]
    assert result["abstract_sentence_score_list"] == [1.0]
    assert result["abstract_sentence_rank_list"] == [1]
    assert result["abstract_sentence_rank_list"] == [1]
    assert result["abstract_sentence_score_list"] == [1.0]
    assert result["abstract_sentence_rank_list"] == [1]
    assert result["abstract_sentence_score_list"] == [1.0]
    assert result["abstract_sentence_rank_list"] == [1]
    assert result["abstract_sentence_score_list"] == [1.0]
    assert result["abstract_sentence_rank_list"] == [1]
    assert result["abstract_sentence_score_list"] == [1.0]
    assert result["abstract_sentence_rank_list"] == [1]
    assert result["abstract_sentence_score_list"] == [1.0]
    assert result["abstract_sentence_rank_list"] == [1]
    assert result["abstract_sentence_score_list"] == [1.0]
    assert result["abstract_sentence_rank_list"] == [1]

#write test functions for the get_sentiment function
def test_get_sentiment():
    # write test code here
    text = "The quick brown fox jumped over the lazy dog."
    result = get_sentiment(text)
    assert result == "The sentiment of the text is: Positive and the Score is: 0.74"
    


