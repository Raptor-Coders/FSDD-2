import { IcourseInterface } from './icourse.interface';

export const COURSES: IcourseInterface[] = [
  {
    id: 1,
    title: 'Introduction to Python',
    description: `Learn the fundamentals of Python programming.
                  This course covers topics like data types, control structures,
                  functions, and more.`,
    sessions: 5,
    sessionDuration: 120,
    // startDate: new Date(),
    // endDate: new Date('2023-12-05'),
    tags: ['JavaScript Fundamentals', 'Web Development with Angular'],
    isFeatured: true,
    imageUrl:
      'https://r3.ieee.org/fwc/wp-content/uploads/sites/23/2022/05/Python-Programming.jpg',
  },
  {
    id: 2,
    title: 'Web Development with Angular',
    description: `Build dynamic web applications using Angular.
                  Explore components, services, and routing to create
                  modern web experiences.`,
    sessions: 5,
    sessionDuration: 120,
    tags: ['Introduction to Python', 'JavaScript Fundamentals'],
    isFeatured: true,
    imageUrl:
      'https://miro.medium.com/v2/resize:fit:720/format:webp/1*lqMtWmTLHxT_6SN4Kjvaog.png',
  },
  {
    id: 3,
    title: 'JavaScript Fundamentals',
    description: `Master the basics of JavaScript for web development.
                  Topics include variables, functions, DOM manipulation, and more.`,
    sessions: 5,
    sessionDuration: 120,
    tags: ['Introduction to Python', 'Web Development with Angular'],
    isFeatured: true,
    imageUrl:
      'https://www.freecodecamp.org/news/content/images/size/w2000/2023/04/JavaScript-Blog-Cover.png',
  },
  {
    id: 4,
    title: 'React for Beginners',
    description: `Get started with React and build interactive user interfaces.
                  Dive into components, state management, and hooks.`,
    sessions: 5,
    sessionDuration: 120,
    tags: [
      'Node.js Backend Development',
      'Mobile App Development with Flutter',
    ],
    isFeatured: true,
    imageUrl:
      'https://repository-images.githubusercontent.com/37153337/9d0a6780-394a-11eb-9fd1-6296a684b124',
  },
  {
    id: 5,
    title: 'Node.js Backend Development',
    description: `Learn to build server-side applications with Node.js.
                  Topics include HTTP, Express.js, and database integration.`,
    sessions: 5,
    sessionDuration: 120,
    tags: ['React for Beginners', 'Mobile App Development with Flutter'],
    isFeatured: true,
    imageUrl:
      'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Node.js_logo.svg/1200px-Node.js_logo.svg.png',
  },
  {
    id: 6,
    title: 'Mobile App Development with Flutter',
    description: `Create cross-platform mobile apps using Flutter.
                  Explore widgets, state management, and app deployment.`,
    sessions: 5,
    sessionDuration: 120,
    tags: ['Node.js Backend Development', 'React for Beginners'],
    isFeatured: true,
    imageUrl:
      'https://storage.googleapis.com/cms-storage-bucket/70760bf1e88b184bb1bc.png',
  },
];
