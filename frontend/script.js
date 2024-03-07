const taskForm = document.getElementById('task-form');
const pendingList = document.getElementById('pending-list');
const progressList = document.getElementById('progress-list');
const completeList = document.getElementById('complete-list');

taskForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const title = document.getElementById('task-title').value;
  const description = document.getElementById('task-description').value;
  const task = createTask(title, description);
  pendingList.appendChild(task);
  taskForm.reset();
});

function createTask(title, description) {
  const task = document.createElement('li');
  task.className = 'task-item';

  const titleElement = document.createElement('span');
  titleElement.className = 'task-title';
  titleElement.textContent = title;
  task.appendChild(titleElement);

  const descriptionElement = document.createElement('span');
  descriptionElement.textContent = description;
  task.appendChild(descriptionElement);

  const actions = document.createElement('div');
  actions.className = 'task-actions';

  const progressButton = document.createElement('button');
  progressButton.className = 'task-action-button';
  progressButton.textContent = 'In Progress';
  progressButton.addEventListener('click', () => {
    progressList.appendChild(task);
  });
  actions.appendChild(progressButton);

  const completeButton = document.createElement('button');
  completeButton.className = 'task-action-button';
  completeButton.textContent = 'Complete';
//   completeButton.addEventListener('click', () => {
//     complete
}