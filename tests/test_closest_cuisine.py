import sys
sys.path.append('..')
import project2 
def test_closest_cuisines():
    input_ingredients = ['rice', 'fish']
    N = 10
    predicted_result, closest_cuisines  = project2.main(N, input_ingredients)


    assert len(closest_cuisines) == 10
