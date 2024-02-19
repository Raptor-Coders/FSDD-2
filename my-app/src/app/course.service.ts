import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, map } from 'rxjs';
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

  getAllCourses(): Observable<IcourseInterface[]> {
    return this.http.get<IcourseInterface[]>(this.coursesUrl);
  }

  getFeaturedCourses(): Observable<IcourseInterface[]> {
    return this.getAllCourses().pipe( map( courses => courses.filter(course => course.isFeatured) ) );
  }

  getCourseById(id: number): Observable<IcourseInterface> {
    return this.http.get<IcourseInterface>(`${this.coursesUrl}/${id}/`);
  }
} // end class

export function getMyName2() {
  return 'Dele2';
}
