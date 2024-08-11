/* global $ */
$(function () {
  const newElement = '<li>Item</li>';
  const list = $('UL.my_list');

  function addElement () {
    list.append(newElement);
  }
  function removeElemet () {
    $('UL.my_list li:last-child').remove();
  }
  function clearElement () {
    list.empty();
  }

  $('DIV#add_item').click(addElement);
  $('DIV#remove_item').click(removeElemet);
  $('DIV#clear_list').click(clearElement);
});
