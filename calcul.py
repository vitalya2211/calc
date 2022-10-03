import module
import view
def button_click():
    val_a=view.get_value()
    val_b=view.get_value()
    module.init(val_a,val_b)
    result=module.sum()
    view.view_val(result)
