"""Test functions for contour command."""

from easyviztest import *


class test_contour_basic(EasyvizTestCase):
    def check_contour_default(self):
        x,y,xv,yv,values = self.get_2D_data()
        contour(xv,yv,values)
        title("contour(xv,yv,values)")
        n()

    def check_contour_no_grid_components(self):
        x,y,xv,yv,values = self.get_2D_data()
        contour(values)
        title("contour(values)")
        n()

    def check_contour_1D_grid_components(self):
        x,y,xv,yv,values = self.get_2D_data()
        contour(x,y,values)
        title("contour(x,y,values)")
        n()

    def check_contour_not_sparse_grid(self):
        x,y,xv,yv,values = self.get_2D_data(sparse=False)
        contour(xv,yv,values)
        title("contour(xv,yv,values) (xv and yv not sparse)")
        n()


class test_contour_levels(EasyvizTestCase):
    def check_contour_5_levels(self):
        x,y,xv,yv,values = self.get_2D_data()
        contour(xv,yv,values,5)
        title("contour(xv,yv,values,5)")
        n()

    def check_contour_15_levels_kwarg(self):
        x,y,xv,yv,values = self.get_2D_data()
        contour(xv,yv,values,clevels=15)
        title("contour(xv,yv,values,clevels=15)")
        n()

    def check_contour_specify_levels(self):
        x,y,xv,yv,values = self.get_2D_data()
        contour(xv,yv,values,[-3, -1, 1, 5])
        title("contour(xv,yv,values,[-3, -1, 1, 5])")
        n()

    def check_contour_specify_levels_kwarg(self):
        x,y,xv,yv,values = self.get_2D_data()
        contour(xv,yv,values,cvector=linspace(-10,10,10))
        title("contour(xv,yv,values,cvector=linspace(-10,10,10))")
        n()


class test_contour_memoryorder_xyz(EasyvizTestCase):
    def check_contour_memoryorder_xyz_default(self):
        x,y,xv,yv,values = self.get_2D_data(memoryorder='xyz')
        contour(xv,yv,values,memoryorder='xyz')
        title("contour(xv,yv,values,memoryorder='xyz')")
        n()
        
    def check_contour_memoryorder_xyz_rectangular_grid(self):
        x = linspace(-3,3,21)
        y = linspace(-2,2,13)
        xv, yv = meshgrid(x, y, memoryorder='xyz')
        values = peaks(xv,yv)
        contour(xv,yv,values,memoryorder='xyz')
        title("contour(xv,yv,values,memoryorder='xyz') (rectangular grid)")
        n()
        
    def check_contour_memoryorder_xyz_rectangular_grid2(self):
        x = linspace(-5,5,21)
        y = linspace(-2,2,31)
        xv, yv = meshgrid(x, y, memoryorder='xyz')
        values = peaks(xv,yv)
        contour(xv,yv,values,memoryorder='xyz')
        title("contour(xv,yv,values,memoryorder='xyz') (rectangular grid)")
        n()


class test_contour_misc(EasyvizTestCase):
    def check_contour_12_levels_format_string(self):
        x,y,xv,yv,values = self.get_2D_data()
        contour(xv,yv,values,12,'r--')
        title("contour(xv,yv,values,12,'r--')")
        n()

    def check_contour_format_string(self):
        x,y,xv,yv,values = self.get_2D_data()
        contour(xv,yv,values,'b:')
        title("contour(xv,yv,values,'b:')")
        n()

    def check_contour_linewidth(self):
        x,y,xv,yv,values = self.get_2D_data()
        contour(xv,yv,values,linewidth=3)
        title("contour(..,linewidth=3)")
        n()


class test_contour_labels(EasyvizTestCase):
    def check_contour_labels(self):
        x,y,xv,yv,values = self.get_2D_data()
        contour(xv,yv,values)
        clabel('on')  # FIXME: this is broken
        title("contour(..);clabel('on')")
        n()

    def check_contour_labels_off(self):
        x,y,xv,yv,values = self.get_2D_data()
        contour(xv,yv,values)
        clabel('on')
        clabel('off')
        title("contour(..);clabel('on');clabel('off')")
        n()

    def check_contour_labels_kwarg(self):
        x,y,xv,yv,values = self.get_2D_data()
        contour(xv,yv,values,clabel='on') 
        title("contour(..,clabel='on')")
        n()


def test_suite(level=1):
    suites = []
    if level > 0:
        suites.append(unittest.makeSuite(test_contour_basic,'check_'))
        suites.append(unittest.makeSuite(test_contour_levels,'check_'))
        suites.append(unittest.makeSuite(test_contour_memoryorder_xyz,
                                         'check_'))
        suites.append(unittest.makeSuite(test_contour_misc,'check_'))
        suites.append(unittest.makeSuite(test_contour_labels,'check_'))
    total_suite = unittest.TestSuite(suites)
    return total_suite

def test(level=10):
    all_tests = test_suite()
    runner = unittest.TextTestRunner()
    runner.run(all_tests)
    return runner

if __name__ == "__main__":
    test()
    raw_input("press enter to exit")