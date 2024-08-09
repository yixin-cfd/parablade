from TestCase import TestCase 
import sys 

def main():
    
    test_list:list[TestCase] = [] 

    # 2D turbine blade surface generation
    turbine_2D = TestCase("turbine_2D")
    turbine_2D.config_dir = "BladeProfiles/2D_examples/turbine_2D/"
    turbine_2D.config_file = "turbine_2D.cfg"
    turbine_2D.exec_command = "MakeBlade.py"
    turbine_2D.reference_files = ["blade_surface.ref"]
    turbine_2D.test_files = ["coordinates/blade_surface.csv"]
    test_list.append(turbine_2D)

    # 2D compressor blade surface generation and sensitivity computation
    compressor_2D = TestCase("compressor_2D")
    compressor_2D.config_dir = "BladeProfiles/2D_examples/compressor_2D/"
    compressor_2D.config_file = "compressor_2D.cfg"
    compressor_2D.exec_command = "MakeBlade.py"
    compressor_2D.reference_files = ["blade_surface.ref", "blade_surface_grad_theta_in_0.ref"]
    compressor_2D.test_files = ["coordinates/blade_surface.csv", "CAD_SENSITIVITY/blade_surface_grad_theta_in_0.csv"]
    test_list.append(compressor_2D)

    pass_list = [test.run_test() for test in test_list]

    # Tests summary
    print('==================================================================')
    print('Summary of the serial tests')
    print('python version:', sys.version)
    for i, test in enumerate(test_list):
        if (pass_list[i]):
            print('  passed - %s'%test.tag)
        else:
            print('* FAILED - %s'%test.tag)

    if all(pass_list):
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()
