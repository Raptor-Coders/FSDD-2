import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { COURSES } from './courses-data';
import { IcourseInterface } from './icourse.interface';

@Injectable({
  providedIn: 'root',
})
export class CourseService {
  private coursesUrl = 'http://localhost:8000/api/courses';
  // private coursesUrl = 'https://www.raptorcoders.com/api/courses/';

  constructor(private http: HttpClient) {}

  getMyName() {
    // this.httpClient.get('/api/courses');
    return 'Dele';
  }

  getFeaturedCourses() {
    const featuredCourses: IcourseInterface[] = [];
    for (const course of COURSES) {
      if (course.isFeatured) {
        featuredCourses.push(course);
      }
    }
    return featuredCourses;
  }

  getAllCourses(): Observable<IcourseInterface[]> {
    return this.http.get<IcourseInterface[]>(this.coursesUrl);
  }

  // getAllCourses(): IcourseInterface[] {
  //   // const allCourses: IcourseInterface[] = [];
  //   // for (const course of COURSES) {
  //   //   allCourses.push(course);
  //   // }
  //   return COURSES;
  // }

  getCourseById(id: number): Observable<IcourseInterface> {
    return this.http.get<IcourseInterface>(`${this.coursesUrl}/${id}/`);
  }



  // getCourseById(id: number): IcourseInterface | undefined {
  //   return COURSES.find((course) => course.id === id);
  // }
} // end class

export function getMyName2() {
  return 'Dele2';
}
