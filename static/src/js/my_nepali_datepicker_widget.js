/** @odoo-module **/
import { registry } from "@web/core/registry";
import { useInputField } from "@web/views/fields/input_field_hook";
import time from 'web.time';
var translation = require('web.translation');
var _t = translation._t;
const { Component,useRef} = owl;

export class DomainSelectorTextField extends Component {
   static template = 'FieldDateMultipleDate'
   setup(){
       super.setup();
       this.input = useRef('inputdate')
       useInputField({ getValue: () => this.props.value || "", refName: "inputdate" });
   }
   _onSelectDateField(ev){
       var dateFormat = time.getLangDateFormat();
      if (dateFormat.includes('MMMM')){
         var dates = dateFormat.toLowerCase()
         var result = dates.replace(/mmmm/g, 'MM');
         dateFormat = result
     }
     else if (dateFormat.includes('MMM')) {
         var dates = dateFormat.toLowerCase()
         var result = dates.replace(/mmm/g, 'M');
         dateFormat = result
     }
     else if(dateFormat.includes('ddd')){
         var dates =new dateFormat.toLowerCase()
         var result = new dates.replace(/ddd/g, 'DD');
         dateFormat = result
     }
    else{
       dateFormat = dateFormat.toLowerCase()
    }
       if (this.input.el){
          this.props.update(this.input.el.value.replace(DomainSelectorTextField, ''));
           console.log('this',dateFormat)
           $(this.input.el).nepaliDatePicker({
               multidate: true,
               dateFormat: dateFormat,
               closeOnDateSelect: true
           }).trigger('focus');
       }
   }
}

registry.category("fields").add("multiple_datepicker", DomainSelectorTextField);