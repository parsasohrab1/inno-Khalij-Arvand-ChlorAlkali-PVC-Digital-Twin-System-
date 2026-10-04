# feedback_recording.py
# Recording real feedback for model retraining

def record_feedback(feedback_type, value, note=""):
    """
    Record real feedback.
    
    Input:
        feedback_type: feedback type (membrane replacement or washing)
        value: the recorded real value
        note: additional description
    """
    feedback = {
        "type": feedback_type,
        "value": value,
        "note": note
    }
    print("Feedback recorded:", feedback)
    return feedback

if __name__ == "__main__":
    record_feedback("Membrane replacement", "1405-07-15", "The membrane of cell 3 was replaced.")
    record_feedback("Washing", "1405-07-20", "Autoclave 2 was washed.")
