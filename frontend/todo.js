document.addEventListener('DOMContentLoaded', function () {
   const addTaskBtn = document.getElementById('add-task-btn');
   const taskTitleInput = document.getElementById('task-title');
   const taskDescriptionInput = document.getElementById('task-description');
   const taskDateInput = document.getElementById('task-date');
   const taskList = document.getElementById('task-list');
   const partitions = document.querySelectorAll('.partition');
   let taskId = 0;
   addTaskBtn.addEventListener('click', function () {
       const title = taskTitleInput.value.trim();
       const description = taskDescriptionInput.value.trim();
       const date = taskDateInput.value;
       if (title && description && date) {
           data={title:title,description:description,date:date};
           const task = createTaskElement(title, description, date);
           const partition = partitions[0];
           partition.appendChild(task);
           updateTaskCount(partition);
           taskTitleInput.value = '';
           taskDescriptionInput.value = '';
           taskDateInput.value = '';
           addTaskBtn.innerHTML="Add Task";
       }
   });

   function createTaskElement(title, description, date) {
       const taskItem = document.createElement('div');
       taskItem.classList.add('task-item');
       taskItem.dataset.id = taskId++;
       taskItem.innerHTML = `
           <h3>${title}</h3>
           <p>${description}</p>
           <p class="task-date">Date: ${date}</p>
           <button class="edit-btn">Edit</button>
           <button class="delete-btn">Delete</button>
       `;
       taskItem.querySelector('.delete-btn').addEventListener('click', function () {
           taskItem.remove();
           updateTaskCount(taskItem.parentNode);
       });
       taskItem.querySelector('.edit-btn').addEventListener('click', function () {
           taskTitleInput.value = title;
           taskDescriptionInput.value = description;
           taskDateInput.value = date;
           addTaskBtn.innerHTML="Update Task"
           taskItem.remove();
           updateTaskCount(taskItem.parentNode);
       });
       makeTaskDraggable(taskItem);
       return taskItem;
   }

   function makeTaskDraggable(taskItem) {
       taskItem.draggable = true;
       taskItem.addEventListener('dragstart', function (event) {
           event.dataTransfer.setData('text/plain', event.target.dataset.id);
       });
   }

   partitions.forEach(partition => {
       partition.addEventListener('dragover', function (event) {
           event.preventDefault();
       });

       partition.addEventListener('drop', function (event) {
           event.preventDefault();
           const taskId = event.dataTransfer.getData('text/plain');
           console.log(taskId);
           const taskItem = document.querySelector(`.task-item[data-id="${taskId}"]`);
           console.log(taskItem);
           const sourcePartition = taskItem.parentNode;
           console.log(sourcePartition);
           if (partition !== sourcePartition) {
               partition.appendChild(taskItem);
               updateTaskCount(partition);
               updateTaskCount(sourcePartition);
           }
       });
   });

   function updateTaskCount(partition) {
       const taskCount = partition.querySelectorAll('.task-item').length;
       partition.querySelector('h2').textContent = partition.dataset.partition.replace('-', ' ') + ` (${taskCount})`;
   }
});