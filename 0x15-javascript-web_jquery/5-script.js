/* global $ */
// $(document).ready(function() {
//     add.click()
// });
function addElement () {
  const list = $('UL.my_list');
  const element = '<li>Item</li>';
  list.append(element);
}
$('DIV#add_item').click(addElement);
