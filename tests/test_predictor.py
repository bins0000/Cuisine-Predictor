import sys
sys.path.append('..')
import project2 
def test_predictor():
    input_ingredients = ['rice', 'fish']
    N = 5 
    predicted_result, closest_cuisines  = project2.main(N, input_ingredients)
    

    assert len(predicted_result) == 1
